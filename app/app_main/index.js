const express = require('express')
const app = express()

// Get
app.get('/', (req, res) => {
    res.send('Get request');
});

// Post
app.post('/', (req, res) => {
    res.send('Post request')
});

// Put
app.put('/', (req, res) => {
    res.send('Put request');
});

// Delete
app.delete('/', (req, res) => {
    res.send('Delete request');
});

app.listen(3000, () => console.log('listen get/post/put/delete request at port 3000'))