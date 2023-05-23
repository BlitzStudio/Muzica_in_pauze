import express from "express";
import morgan from "morgan";
import cookieParser from "cookie-parser";
import mongoose from "mongoose";
import cors from "cors";
const app = express();
import "dotenv/config";
import api from "./api.js";

const PORT = process.env.PORT;
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(morgan("dev"));
app.use(cookieParser(process.env["COOKIE_SECRET"]));
app.use(
  cors({
    origin: "http://localhost:8080",
    credentials: true,
  })
);

mongoose
  .connect("mongodb://localhost:27017/pauzeMuzicale")
  .then(() => {
    console.log("DATABASE:Online");
  })
  .catch((err) => {
    console.log("DATABASE:Offline");
    console.log(err);
  });

app.use("/api", api);

app.get("/", (req, res) => {
  res.send("<h1>Hello World</h1>");
});

app.use((err, req, res, next) => {
  const { status = 500, message = "Server error" } = err;
  res.status(status).send(message);
});

app.listen(PORT, () => {
  console.log(`App is listening on http://localhost:${PORT}`);
});
