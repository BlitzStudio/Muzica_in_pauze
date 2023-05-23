import express from "express";
import morgan from "morgan";
import cookieParser from "cookie-parser";
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

app.use("/api", api);

app.get("/", (req, res) => {
  console.log(req.signedCookies);
  res.send("<h1>Hello World</h1>");
});

app.listen(PORT, () => {
  console.log(`App is listening on http://localhost:${PORT}`);
});
