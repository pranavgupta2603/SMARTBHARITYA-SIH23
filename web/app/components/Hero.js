import React from "react";

export const Hero = () => {
  // todo: assign all colors to variables
  // todo: Link buttons to redirecting functions/make them links
  return (
    <div className="h-[600px] w-[1100px] flex flex-col justify-around items-center">
      <h1 className="text-heroColor text-[120px] font-bold text-center">
        Misk-AK
      </h1>
      <p className="text-[#ccc] text-[35px] text-center">
        AI-ML based intelligent de-smoking/de-hazing algorithm
      </p>
      <div className="button w-[523px] h-[98px] bg-customPink rounded-full flex justify-center items-center">
        <p className="text-[#051937] text-[55px] font-bold">DeHaze</p>
      </div>
      <div className="button w-[273px] h-[53px] border border-customOrange flex justify-center items-center rounded-full">
        <p className="text-customOrange text-[25px] font-bold">About us</p>
      </div>
    </div>
  );
};
