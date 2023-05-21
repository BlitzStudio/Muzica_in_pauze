import jwtDecode from "jwt-decode";
import axios from "./axios";

export async function loginController(setState, ticket) {
  let token;
  console.log(ticket);
  if (ticket) {
    token = await axios
      .post(
        "/api/login",
        {
          ticket,
        },
        {
          withCredentials: true,
        }
      )
      .then((data) => {
        console.log(data);
      });
    // daca utilizatorul se logheaza
  } else {
  }
}
