const express = require("express");
const redis = require("redis");

const app = express();
const redisClient = redis.createClient({ host: "redis", port: 6379 });

app.get("/", async (req, res) => {
    redisClient.incr("visits");
    redisClient.get("visits", (err, visits) => {
        res.send(`🚀 Express + Redis! Visit count: ${visits}`);
    });
});

app.listen(3000, () => console.log("🚀 Server running on port 3000"));
