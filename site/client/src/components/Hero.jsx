export const Hero = () => {
  return (
    <header className="relative ">
      <img
        className="absolute inset-0 object-cover w-full h-full "
        src="https://cnaic.ro/wp-content/uploads/2019/12/slider-bg.jpg"
        alt=""
        srcset=""
      />
      <div className="relative min-h-[100vh]">
        <svg
          className="absolute inset-x-0 bottom-0 text-white fill-[#f5f5f5]"
          viewBox="0 0 1160 163"
        >
          <path d="M-164 13L-104 39.7C-44 66 76 120 196 141C316 162 436 152 556 119.7C676 88 796 34 916 13C1036 -8 1156 2 1216 7.7L1276 13V162.5H1216C1156 162.5 1036 162.5 916 162.5C796 162.5 676 162.5 556 162.5C436 162.5 316 162.5 196 162.5C76 162.5 -44 162.5 -104 162.5H-164V13Z" />
        </svg>
        <div className="relative px-8 py-16 text-white flex flex-col items-start justify-center w-[100%] h-[100vh]">
          <div className="max-w-[450px] ml-8 px-4 bg-white bg-opacity-20 backdrop-blur-lg text-gray-900 rounded-md py-6">
            <h1 className=" font-bold  text-3xl mb-3  ">
              Pauze <span className="text-purple-800">muzicale</span>
            </h1>
            <p className="text-base text-gray-900  md:text-lg mb-5 mr-8">
              Școala noastră este un loc vibrant, plin de energie și
              creativitate, iar în timpul pauzelor, holurile liceului se
              transformă într-un adevărat spectacol muzical. Sunetele
              încântătoare ale instrumentelor și vocile talentate ale elevilor
              se întrepătrund într-un cadru plin de bucurie și entuziasm.
            </p>
            <a
              className="px-4 py-2 text-white font-medium tracking-wide bg-purple-800 rounded-sm"
              href=""
            >
              Google Btn
            </a>
            <a className="px-4 py-2 font-medium tracking-wide " href="">
              Afla mai multe
            </a>
          </div>
        </div>
      </div>
    </header>
  );
};

// cnaic img
/* <img
          className=" object-cover w-full  h-[100%] "
          src="https://cnaic.ro/wp-content/uploads/2019/12/slider-bg.jpg"
          alt=""
          srcset=""
        /> */
