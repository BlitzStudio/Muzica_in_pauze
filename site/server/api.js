import express from "express";
import { OAuth2Client } from "google-auth-library";
import { googleIdentity } from "./utils/auth.js";

const router = express.Router();

router.post("/login", async (req, res) => {
  const { ticket } = req.body;
  const userData = await googleIdentity(ticket).catch(() => {
    res.status(401).send("This is not a valid Google account ");
  });
  res
    .cookie("tk", "isLoggedIn", {
      path: "/",
      httpsOnly: true,
      signed: true,
    })
    .json({ name: userData.name, picture: userData.picture })
    .send("User logged in");
});

export default router;
