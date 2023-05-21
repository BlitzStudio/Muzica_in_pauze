import express from "express";
import { OAuth2Client } from "google-auth-library";
const client = new OAuth2Client(process.env["GOOGLE_ID"]);

const router = express.Router();

router.post("/login", async (req, res) => {
  client
    .verifyIdToken({
      idToken: req.body.ticket,
      audience: process.env["GOOGLE_ID"],
    })

    .then((user) => {
      res.cookie("tk", "isLoggedIn", {
        path: "/",
        httpsOnly: true,
        signed: true,
      });
      const data = {
        name: user.name,
        picture: user.picture,
      };
      console.log(data);
      res.json(data);
    })
    .catch((err) => {
      console.log("Error: \n" + err);
    });
});

export default router;
