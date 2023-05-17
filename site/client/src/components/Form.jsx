const Form = () => {
  return (
    <div className=" rounded-md bg-white  bg-opacity-10 px-6 py-12 text-gray-900 backdrop-blur-md ">
      <h2 className="mb-1 text-xl font-semibold">Note muzicale</h2>
      <p className="mb-1 text-sm text-gray-900">
        Completeaza formularul de mai jos pentru a iti auzi melodiile preferate
        in timpul pauzelor
      </p>
      <form className="flex flex-col  " action="" method="post">
        <input className="mb-2 mr-2 block rounded-sm bg-white/50 p-1 outline outline-1" />
        <input className="mb-2 mr-2 block rounded-sm bg-white/50 p-1 outline outline-1" />
        <input className="mb-2 mr-2 block rounded-sm bg-white/50 p-1 outline outline-1" />
        <a
          className="mt-auto self-start  rounded-sm bg-purple-800 px-4 py-2 font-medium tracking-wide text-white"
          href=""
        >
          Google Btn
        </a>
      </form>
    </div>
  );
};

export default Form;
