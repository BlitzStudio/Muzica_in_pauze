const Form = () => {
  return (
    <div className="max-w-[450px] mr-8 px-4 bg-white bg-opacity-10 backdrop-blur-md text-gray-900 rounded-md py-6 h-[350px]">
      <h2 className="font-semibold text-xl mb-1">Note muzicale</h2>
      <p className="text-sm text-gray-900 mb-1">
        Completeaza formularul de mai jos pentru a iti auzi melodiile preferate
        in timpul pauzelor
      </p>
      <form className="flex flex-col  " action="" method="post">
        <input className="bg-white/50 outline outline-1 block mr-2 mb-2 rounded-sm p-1" />
        <input className="bg-white/50 outline outline-1 block mr-2 mb-2 rounded-sm p-1" />
        <input className="bg-white/50 outline outline-1 block mr-2 mb-2 rounded-sm p-1" />
        <a
          className="self-start mt-auto  px-4 py-2 text-white font-medium tracking-wide bg-purple-800 rounded-sm"
          href=""
        >
          Google Btn
        </a>
      </form>
    </div>
  );
};

export default Form;
