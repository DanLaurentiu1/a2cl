import Link from "next/link";
import { Plan } from "../../domain/Plan";
import ProgressBar from "./ProgressBar";

export default function PlanCard(plan: Plan) {
  const topics = Array.from(plan.topics);
  return (
    <Link href={`/plans/${plan.id}`}>
      <div className="flex flex-col bg-lightgrey p-6 rounded-lg items-center">
        {ProgressBar(plan)}
        <h3 className="text-xl font-bold text-white mb-2">{plan.title}</h3>
        <div className="flex flex-wrap gap-2">
          {topics.map((topic) => (
            <span
              key={plan.id}
              className="bg-darkgrey text-white text-xs px-3 py-1 rounded-full"
            >
              {topic.name}
            </span>
          ))}
        </div>
      </div>
    </Link>
  );
}
