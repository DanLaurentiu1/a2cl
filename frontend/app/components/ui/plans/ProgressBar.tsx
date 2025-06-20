import { Plan } from "@/app/lib/domain/Plan";

export default function ProgressBar({ plan }: { plan: Plan }) {
  return (
    <div className="w-full bg-gray-300 rounded-full h-2 mb-4">
      <div
        className="bg-lightgreen h-2 rounded-full"
        style={{ width: `${plan.getPercentageCompleted()}%` }}
      ></div>
    </div>
  );
}
