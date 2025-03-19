import { instatiatePlaceholderData } from "../../domain/plans";
import Link from "next/link";

export default function PlansList() {
  const [topics, problems, profiles, plans] = instatiatePlaceholderData();
  return (
    <div className="">
      {plans.map((plan) => (
        <Link className="" href={`/plans/${plan.id}`}>
          <li key={plan.id}>{plan.title}</li>
        </Link>
      ))}
    </div>
  );
}
