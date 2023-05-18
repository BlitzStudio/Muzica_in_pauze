import Form from "./Form";

const Hero = () => {
  return (
    <div className="headerImage flex min-h-[100vh] items-center justify-center ">
      <header className="grid gap-8  bg-cover   bg-center bg-no-repeat p-4 lg:grid-cols-2">
        <div className="m-4  rounded-md bg-white bg-opacity-10 px-4  py-8 text-gray-900 backdrop-blur-md">
          <h1 className="mb-3  text-3xl font-bold  ">
            Pauze <span className="text-purple-800">muzicale</span>
          </h1>
          <p className="mb-5 mr-8  text-base text-gray-900 md:text-lg">
            Școala noastră este un loc vibrant, plin de energie și creativitate,
            iar în timpul pauzelor, holurile liceului se transformă într-un
            adevărat spectacol muzical. Sunetele încântătoare ale instrumentelor
            și vocile talentate ale elevilor se întrepătrund într-un cadru plin
            de bucurie și entuziasm.
          </p>

          <a
            className="rounded-sm bg-purple-800 px-4 py-2 font-medium tracking-wide text-white"
            href=""
          >
            Google Btn
          </a>
          <a className="px-4 py-2 font-medium tracking-wide " href="">
            Afla mai multe
          </a>
        </div>
        <Form />
      </header>
    </div>
  );
};

export default Hero;
