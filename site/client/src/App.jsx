import Hero from "./components/Hero";
import { loginController } from "./api/auth";
import { useState, useEffect } from "react";
const App = function () {
  const [user, setUser] = useState({});
  useEffect(() => {
    loginController(setUser);
  }, []);
  return (
    <div className="box-border ">
      <Hero setUser={setUser} />
    </div>
  );
};
export default App;
