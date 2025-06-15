"use client";
import Link from "next/link";
import { FaTrash } from "react-icons/fa";
import { usePlans } from "../../providers/PlanProvider";

export default function PlansList() {
  const { plans, loading, error, deletePlan } = usePlans();

  const handleDelete = (planId: number) => {
    deletePlan(planId);
  };

  if (loading) return <div>Loading plans...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="flex flex-col flex-grow overflow-auto m-1">
      <ul className="p-1">
        {plans.map((plan, index) => (
          <li
            key={plan.id || `plan-${index}`}
            className="flex justify-between items-center mb-2 text-white bg-lightgrey backdrop-blur-sm p-2 rounded-2xl hover:bg-white/20 transition-all duration-10 cursor-pointer"
          >
            <Link href={`/plans/${plan.id}`}>
              <span className="text-white">{plan.title}</span>
            </Link>
            <button
              className="text-white bg-lightgrey p-2 rounded-3xl border-2 border-lightgreen font-semibold flex items-center justify-center hover:border-orange transition-all duration-200"
              aria-label="Delete plan"
              onClick={() => handleDelete(plan.id)}
            >
              <FaTrash className="w-3 h-3" />
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
