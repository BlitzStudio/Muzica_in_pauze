import { Hero } from "./components/Hero";

const App = function () {
  return (
    <div className="box-border">
      <Hero />
      {/* <div className="bg-red-900 grid grid-cols-2 ">
        <div className="h-[300px] w-[300px] rounded-full bg-blue-500 flex justify-center items-center">
          .
        </div>
        <div className="h-[300px] w-[300px] rounded-full bg-blue-500">.</div>
      </div> */}
    </div>
  );
};
export default App;
