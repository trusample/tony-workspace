async function api(action, params) {
    const res = await fetch(API_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action, params: params || {} })
    });
    return await res.json();
}

function switchTab(evt, tabName) {
    if (tabName === 'contacts') {
        loadContacts();
    }
    // ... other tab switches
}