import Link from "next/link";
import { plans } from "../../domain/data";
import PlanCard from "@/app/ui/plans/PlanCard";

export default function AllPlans() {
  return (
    <div className="p-8 grid grid-cols-4 gap-32">
      {plans.map((plan) => PlanCard(plan))}
    </div>
  );
}
