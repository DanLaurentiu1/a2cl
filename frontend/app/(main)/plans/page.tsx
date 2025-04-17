"use client";
import { usePlans } from "@/app/components/providers/PlanProvider";
import PlanCard from "@/app/components/ui/plans/PlanCard";
import { useState } from "react";

export default function AllPlans() {
  const { plans, loading, error } = usePlans();
  const [sortByName, setSortByName] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const [plansPerPage] = useState(8);

  if (loading) return <div>Loading plans...</div>;
  if (error) return <div>Error: {error}</div>;
  const displayedPlans = sortByName
    ? [...plans].sort((a, b) => a.title.localeCompare(b.title))
    : plans;

  const indexOfLastPlan = currentPage * plansPerPage;
  const indexOfFirstPlan = indexOfLastPlan - plansPerPage;
  const currentPlans = displayedPlans.slice(indexOfFirstPlan, indexOfLastPlan);
  const paginate = (pageNumber: number) => setCurrentPage(pageNumber);
  const totalPages = Math.ceil(displayedPlans.length / plansPerPage);

  return (
    <div className="p-8">
      <button
        onClick={() => {
          setSortByName(!sortByName);
          setCurrentPage(1);
        }}
        className="mb-4 text-white w-32 bg-darkgrey p-1 rounded-3xl border-2 border-lightgreen font-semibold flex items-center justify-center hover:border-orange transition-all duration-200"
      >
        {sortByName ? "Unsort" : "Sort"}
      </button>
      <div className="grid grid-cols-4 gap-32">
        {currentPlans.map((plan, index) => (
          <PlanCard key={plan.id || `plan-${index}`} plan={plan} /> //fallback key
        ))}
      </div>
      <div className="fixed bottom-4 left-68 right-0 flex justify-center items-center">
        <button
          onClick={() =>
            setCurrentPage((currentPage) => Math.max(currentPage - 1, 1))
          }
          disabled={currentPage === 1}
          className="mr-10 text-white w-26 bg-darkgrey p-1 rounded-3xl border-2 border-lightgreen font-semibold flex items-center justify-center hover:border-orange transition-all duration-200 disabled:opacity-50"
        >
          Previous
        </button>
        {Array.from({ length: totalPages }, (_, i) => i + 1).map((number) => (
          <button
            key={number}
            onClick={() => paginate(number)}
            className={`mx-1 px-3 py-1 rounded ${
              currentPage === number
                ? "bg-lightgreen text-white"
                : "bg-darkgrey text-white"
            }`}
          >
            {number}
          </button>
        ))}
        <button
          onClick={() =>
            setCurrentPage((currentPage) =>
              Math.min(currentPage + 1, totalPages)
            )
          }
          disabled={currentPage === totalPages}
          className="ml-10 text-white w-26 bg-darkgrey p-1 rounded-3xl border-2 border-lightgreen font-semibold flex items-center justify-center hover:border-orange transition-all duration-200 disabled:opacity-50"
        >
          Next
        </button>
      </div>
    </div>
  );
}
