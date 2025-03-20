import Link from "next/link";
import { FaPlus } from "react-icons/fa";

export default function AddPage() {
  return (
    <div className="flex h-screen rounded-lg justify-center items-center">
      <div className="flex flex-col bg-lightgrey p-6 rounded-lg items-center">
        <p className="text-white text-2xl font-semibold">Create a Plan</p>
        <div className="flex p-2 rounded-lg items-center">
          <input
            type="text"
            placeholder="Profile Name"
            className="p-2 m-4 border-2 border-lightgreen rounded-lg text-white"
          />
          <label className="flex items-center gap-2">
            <input type="checkbox" className="w-5 h-5" />
            <span className="text-white">From Leetcode</span>
          </label>
        </div>
        <div className="flex p-2 w-full gap-12 rounded-lg items-center">
          <input
            type="text"
            placeholder="Topic Name"
            className="p-2 m-4 border-2 border-lightgreen rounded-lg text-white"
          />
          <button className="flex items-center justify-center w-9 h-9 text-white rounded-full border-2 border-lightgreen hover:border-orange transition-all duration-200">
            <FaPlus className="text-base" />
          </button>
        </div>
        <div className="flex p-4 w-5/6 gap-4 rounded-lg items-center">
          <Link
            className="text-white w-5/6 bg-lightgrey p-1 rounded-3xl border-2 border-lightgreen font-semibold flex items-center justify-center hover:border-orange transition-all duration-200"
            href="/plans"
          >
            Choose Topics
          </Link>
          <Link
            className="text-white w-5/6 bg-lightgrey p-1 rounded-3xl border-2 border-lightgreen font-semibold flex items-center justify-center hover:border-orange transition-all duration-200"
            href="/plans"
          >
            Add
          </Link>
        </div>
      </div>
    </div>
  );
}
