import Link from "next/link";
import PlansList from "./PlansList";

export default function SidePannel() {
  return (
    <div className="flex flex-col w-1/7 bg-lightgrey rounded-r-2xl p-2 h-screen">
      <div className="flex text-justify items-center justify-between m-4">
        <h2 className="text-white text-2xl font-semibold">Plans</h2>
        <Link
          href="/"
          className="text-white w-3/5 bg-lightgrey p-1 rounded-3xl border-2 border-lightgreen font-semibold flex items-center justify-center hover:border-orange transition-all duration-200"
        >
          Home
        </Link>
      </div>
      <PlansList></PlansList>
      <div className="mt-auto flex flex-col space-y-4 items-center">
        <Link
          className="text-white w-5/6 bg-lightgrey p-1 rounded-3xl border-2 border-lightgreen font-semibold flex items-center justify-center hover:border-orange transition-all duration-200"
          href="/plans"
        >
          View all Plans
        </Link>
      </div>
    </div>
  );
}
