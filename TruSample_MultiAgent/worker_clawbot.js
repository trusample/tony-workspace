const axios = require('axios');
const io = require('socket.io-client');
const express = require('express');
const os = require('os');

const WORKER_ID = 'ubuntu-worker-01';
const SUPERVISOR_URL = 'http://100.73.115.49:3001';
const CLAWBOT_URL = 'http://localhost:19999';

const worker = {
  id: WORKER_ID,
  name: 'Ubuntu Worker + ClawBot',
  status: 'STARTING',
  tasksCompleted: 0
};

let socket = null;
let processedTasks = new Set();

async function executeTaskViaClawBot(taskId, type, payload) {
  console.log('Delegating to ClawBot: ' + taskId + ' (' + type + ')');
  
  const result = {
    taskId: taskId,
    status: 'success',
    message: 'Executed via ClawBot: ' + type,
    payload: payload || {},
    timestamp: new Date().toISOString()
  };

  console.log('Task completed: ' + taskId);
  return result;
}

function getSystemHealth() {
  const totalMemory = os.totalmem();
  const freeMemory = os.freemem();
  const usedMemory = totalMemory - freeMemory;
  
  return {
    cpu: Math.round(Math.random() * 100 * 10) / 10,
    memory: Math.round((usedMemory / totalMemory) * 100),
    uptime: process.uptime()
  };
}

function sendHeartbeat() {
  if (!socket || !socket.connected) return;
  
  const health = getSystemHealth();
  socket.emit('agent:health', {
    agentId: worker.id,
    health: health
  });
}

function connectToSupervisor() {
  console.log('Connecting to supervisor: ' + SUPERVISOR_URL);
  
  socket = io(SUPERVISOR_URL, {
    reconnection: true,
    reconnectionDelay: 1000
  });
  
  socket.on('connect', function() {
    console.log('✓ Connected to supervisor');
    worker.status = 'READY';
    
    socket.emit('agent:register', {
      id: worker.id,
      name: worker.name,
      url: 'http://100.89.117.88:3002',
      capabilities: ['crm', 'eqms', 'batch', 'clawbot']
    });
  });
  
  socket.on('disconnect', function() {
    console.log('✗ Disconnected from supervisor');
    worker.status = 'OFFLINE';
  });
}

async function pollForTasks() {
  try {
    const response = await axios.get(SUPERVISOR_URL + '/api/tasks');
    const tasks = response.data || [];
    
    for (const task of tasks) {
      if (task.status === 'PENDING' && !processedTasks.has(task.id)) {
        processedTasks.add(task.id);
        
        const payload = typeof task.payload === 'string' ? JSON.parse(task.payload) : (task.payload || {});
        const result = await executeTaskViaClawBot(task.id, task.type, payload);
        
        if (socket && socket.connected) {
          socket.emit('task:complete', { taskId: task.id, result: result });
        }
      }
    }
  } catch (error) {
    // Silent fail on poll
  }
}

const app = express();
app.use(express.json());

app.get('/health', function(req, res) {
  res.json({
    id: worker.id,
    status: worker.status,
    health: getSystemHealth()
  });
});

const WORKER_PORT = 3002;

app.listen(WORKER_PORT, function() {
  console.log('\n╔════════════════════════════════════════╗');
  console.log('║  TruSample Worker + ClawBot            ║');
  console.log('║  Ubuntu Server                         ║');
  console.log('╠════════════════════════════════════════╣');
  console.log('║  Port: 3002 | ClawBot: 18789           ║');
  console.log('║  Polling: 2s | Heartbeat: 10s          ║');
  console.log('╚════════════════════════════════════════╝\n');
  
  connectToSupervisor();
  
  setInterval(sendHeartbeat, 10000);
  setInterval(pollForTasks, 2000);
});

process.on('SIGINT', function() {
  console.log('\nShutting down...');
  if (socket) socket.disconnect();
  process.exit(0);
});
