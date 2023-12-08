'use strict';

const express = require('express');
// Constants
const PORT = 3000;
const HOST = '0.0.0.0';

const axios = require('axios');

// App
const app = express();
app.use(express.static('public'));
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html'); // Adjust the path to your HTML file
});

app.get('/hello1', (req, res) => {
  res.send('Hello world\n');
});

// Define your API endpoints and routes here
app.get('/api/doctors', async (req, res) => {
  let url  = process.env.DOCTORS_SERVICE_URL;
  console.log('Doctors Service URL:', process.env.DOCTORS_SERVICE_URL);

  try {
    const response = await axios.get(String(`http://localhost:9090/doctors`));
    const doctors = response.data;
    res.json(doctors);
  } catch (error) {
    console.error('Error fetching doctors:', error);
    res.status(500).json({ error: 'Could not fetch doctors' });
  }
});

app.get('/api/appointments', async (req, res) => {
  let url  = process.env.APPOINTMENTS_SERVICE_URL;
  console.log('Appointments Service URL:', url);

  try {
    const response = await axios.get(String(`http://localhost:7070/appointments`));
    const appointments = response.data;
    res.json(appointments);
  } catch (error) {
    console.error('Error fetching appointments:', error);
    res.status(500).json({ error: 'Could not fetch appointments' });
  }
});

app.listen(PORT, HOST); 
console.log(`Running on http://${HOST}:${PORT}`);