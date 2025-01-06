import express from "express";
import bodyParser from "body-parser";
import cors from "cors";
import mongoose from "mongoose";
import "dotenv/config";
import projectRoutes from "./routes/projects.js";
import skilltRoutes from "./routes/skills.js";
import usertRoutes from "./routes/user.js";
import contactRoutes from "./routes/contact.js";

const app = express();

app.get("/", (req, res) => {
  res.send("Hello, Vercel!");
});

module.exports = app;
const corsOptions = {
  origin: process.env.CORS_ORIGIN, // Use the environment variable for the frontend URL
  methods: "GET,POST,PUT,DELETE",
  credentials: true,
};

app.use(cors());
app.use(bodyParser.json({ limit: "30mb", extended: true }));

app.use("/projects", projectRoutes);
app.use("/skills", skilltRoutes);
app.use("/user", usertRoutes);
app.use("/contact", contactRoutes);

const CONNECTION_URL = `mongodb+srv://${process.env.MONGO_USERNAME}:${process.env.MONGO_PASSWORD}@cluster0.vv7aw.mongodb.net/Portfolio?retryWrites=true&w=majority&appName=Cluster0`;
const PORT = process.env.PORT || 5000;

mongoose
  .connect(CONNECTION_URL)
  .then(() =>
    app.listen(PORT, () => console.log(`Server running on port: ${PORT}`))
  )
  .catch((error) => console.log(error.message));
