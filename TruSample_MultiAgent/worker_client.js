const io = require('socket.io-client');
const express = require('express');
const { v4: uuidv4 } = require('uuid');
const os = require('os');

const WORKER_ID = 'ubuntu-worker-01';
const SUPERVISOR_URL = process.env.SUPERVISOR_URL || 'http://100.73.115.49:3001';

const worker = {
  id: WORKER_ID,
  name: 'Ubuntu Worker',
  status: 'STARTING',
  tasksCompleted: 0,
  tasksActive: 0
};

let socket = null;

function connectToSupervisor() {
  console.log("Connecting to supervisor: " + SUPERVISOR_URL);
  
  socket = io(SUPERVISOR_URL, {
    reconnection: true,
    reconnectionDelay: 1000,
    reconnectionDelayMax: 5000,
    reconnectionAttempts: 5
  });
  
  socket.on('connect', function() {
    console.log("Connected to supervisor");
    worker.status = 'READY';
    
    socket.emit('agent:register', {
      id: worker.id,
      name: worker.name,
      url: 'http://100.89.117.88:3002',
      capabilities: ['crm', 'eqms', 'batch']
    });
    
    console.log("Registered as: " + worker.id);
  });
  
  socket.on('disconnect', function() {
    console.log("Disconnected from supervisor");
    worker.status = 'OFFLINE';
  });
  
  socket.on('error', function(error) {
    console.error("Socket error:", error);
  });
}

function getSystemHealth() {
  const totalMemory = os.totalmem();
  const freeMemory = os.freemem();
  const usedMemory = totalMemory - freeMemory;
  
  return {
    cpu: Math.round(Math.random() * 100 * 10) / 10,
    memory: Math.round((usedMemory / totalMemory) * 100),
    tasksActive: worker.tasksActive,
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
  
  console.log("Heartbeat sent - CPU: " + health.cpu + "% | Memory: " + health.memory + "%");
}

const app = express();
app.use(express.json());

app.get('/health', function(req, res) {
  res.json({
    id: worker.id,
    status: worker.status,
    health: getSystemHealth(),
    tasksCompleted: worker.tasksCompleted
  });
});

const WORKER_PORT = 3002;

app.listen(WORKER_PORT, function() {
  console.log("\nWorker listening on port " + WORKER_PORT);
  connectToSupervisor();
  
  setInterval(function() {
    sendHeartbeat();
  }, 10000);
});

process.on('SIGINT', function() {
  console.log('\nShutting down worker...');
  if (socket) socket.disconnect();
  process.exit(0);
});
