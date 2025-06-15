import Link from "next/link";
import ProgressBar from "./ProgressBar";
import TopicTags from "../topics/TopicTags";
import { Plan } from "@/app/lib/domain/Plan";

export default function PlanCard({ plan }: { plan: Plan }) {
  const topics = Array.from(new Set(plan.topics)).slice(0, 6);
  return (
    <Link href={`/plans/${plan.id}`} className="h-full">
      <div className="h-full flex flex-col bg-lightgrey p-6 rounded-lg">
        <ProgressBar plan={plan} />
        <h3 className="text-xl font-bold text-white mb-4 text-center h-16 line-clamp-2">
          {plan.title}
        </h3>
        <div className="flex-1 min-h-[80px] flex flex-wrap content-start justify-center gap-2 overflow-auto">
          <TopicTags topics={topics} />
        </div>
      </div>
    </Link>
  );
}
