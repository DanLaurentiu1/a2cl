import { Plan } from "@/app/domain/Plan";

export default function ProgressBar(plan: Plan) {
  return (
    <div className="w-full bg-gray-300 rounded-full h-2 mb-4">
      <div
        className="bg-lightgreen h-2 rounded-full"
        style={{ width: `${plan.getPercentageCompleted()}%` }}
      ></div>
    </div>
  );
}
