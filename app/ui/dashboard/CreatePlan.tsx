import Link from "next/link";

export default function CreatePlan() {
  return (
    <div>
      <p>Create a new Plan?</p>
      <Link className="" href="/plans/add">
        Add Plan
      </Link>
    </div>
  );
}
