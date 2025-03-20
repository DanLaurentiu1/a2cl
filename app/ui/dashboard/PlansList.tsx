import { plans } from "../../domain/data";
import Link from "next/link";

export default function PlansList() {
  return (
    <div className="flex flex-col flex-grow overflow-auto m-1">
      <ul className="p-1">
        {plans.map((plan) => (
          <Link href={`/plans/${plan.id}`}>
            <li
              key={plan.id}
              className="mb-2 text-white bg-lightgrey backdrop-blur-sm p-2 rounded-2xl hover:bg-white/20 transition-all duration-10 cursor-pointer"
            >
              {plan.title}
            </li>
          </Link>
        ))}
      </ul>
    </div>
  );
}
