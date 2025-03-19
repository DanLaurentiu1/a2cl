import Link from "next/link";
import PlansList from "./PlansList";

export default function SidePannel() {
  return (
    <div className="">
      <div>
        <p>Plans</p>
        <Link className="" href="/">
          Home
        </Link>
      </div>
      <div>
        <PlansList />
      </div>
      <div>
        <Link className="" href="/plans">
          View all Plans
        </Link>
      </div>
    </div>
  );
}
