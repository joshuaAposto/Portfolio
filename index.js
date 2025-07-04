const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors()); // ✅ Enable CORS globally
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const routes = [
    { path: '/', file: 'index.html' },
    { path: '/ss', file: 'ss.html' },
    { path: '/imgur', file: 'Uploader.html' },
    { path: '/shoti', file: 'shoti.html' },
    { path: '/tempmail', file: 'maintenance.html' }
];

routes.forEach(route => {
    app.get(route.path, (req, res) => {
        res.sendFile(path.join(__dirname, 'public', route.file));
    });
});

app.use((req, res, next) => {
    const isServiceDown = false;
    if (isServiceDown) {
        return res.status(502).sendFile(path.join(__dirname, 'public', '502.html'));
    }
    next();
});

app.use((req, res) => {
    res.status(404).sendFile(path.join(__dirname, 'public', '404.html'));
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
