import React from "react";
import Link from "next/link";

const Navbar = () => {
  const navLinks = [
    { name: "Home", href: "/" },
    { name: "Try Dehazing", href: "/" },
    { name: "About us", href: "/" },
  ];
  return (
    <div className="flex items-center justify-center fixed">
      <div className="bg-[#3A3A62] w-[500px] h-[70px] flex justify-around opacity-70 items-center rounded-[15px] text-white">
        {navLinks.map((navlink) => (
          <Link href={navlink.href}>{navlink.name}</Link>
        ))}
      </div>
    </div>
  );
};

export default Navbar;
