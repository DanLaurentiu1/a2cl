import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col h-screen justify-center items-center">
      <p className="text-4xl font-bold mb-8 text-white">Create a new Plan?</p>
      <Link
        className="text-white w-1/2 bg-darkgrey p-1 rounded-3xl border-2 border-lightgreen font-semibold flex items-center justify-center hover:border-orange transition-all duration-200"
        href="/plans/add"
      >
        Add Plan
      </Link>
    </div>
  );
}
