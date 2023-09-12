import Link from "next/link";
import React from "react";
import Navbar from "./components/Navbar";
import { Hero } from "./components/Hero";

const page = () => {
  return (
    <div className="">
      <div className="bg-primary h-screen flex flex-col space-y-[5%]">
        <div className=" h-[70px] flex justify-center items-center pt-10">
          <Navbar />
        </div>
        <div className="hero-section flex justify-center items-center">
          <Hero />
        </div>
      </div>
    </div>
  );
};

export default page;
