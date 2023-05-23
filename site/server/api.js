import express from "express";
import jwt from "jsonwebtoken";
import { googleIdentity } from "./utils/auth.js";

const router = express.Router();

router.post("/login", async (req, res) => {
  const { ticket } = req.body;

  const { email, name, picture } = await googleIdentity(ticket).catch(() => {
    return res
      .status(500)
      .send(
        "Eroare interna nu am putut sa validam existenta acestui cont de Google "
      );
  });

  if (
    email != process.env["GOOGLE_TEST_EMAIL"] ||
    email.includes(process.env["GOOGLE_DOMAIN_CHECK"])
  ) {
    return res
      .status(401)
      .send("This is not an authorized domain for this app");
  }
  const payload = {
    email,
    name,
    picture,
  };

  const token = jwt.sign(payload, process.env["JWT_SECRET"]);

  return res
    .cookie("tk", "isLoggedIn", {
      path: "/",
      httpsOnly: true,
      signed: true,
    })
    .json({ token });
});

export default router;
