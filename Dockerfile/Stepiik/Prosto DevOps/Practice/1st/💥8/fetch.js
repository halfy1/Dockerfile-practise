const fetch = require('node-fetch');

const API_URL = process.env.API_URL || "https://jsonplaceholder.typicode.com/todos/1";
const INTERVAL = parseInt(process.env.FETCH_INTERVAL, 10) || 5000;

console.log(`Starting fetch service. API_URL=${API_URL}, Interval=${INTERVAL}ms`);

(async function run() {
  while (true) {
    try {
      console.log("Fetching data...");
      const response = await fetch(API_URL);
      const data = await response.json();
      console.log("Received JSON:", data);
    } catch (err) {
      console.error("Error fetching data:", err);
    }
    await new Promise(resolve => setTimeout(resolve, INTERVAL));
  }
})();