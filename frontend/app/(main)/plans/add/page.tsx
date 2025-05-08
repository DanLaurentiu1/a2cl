"use client";
import { Plan } from "@/app/lib/domain/Plan";
import { Profile } from "@/app/lib/domain/Profile";
import Link from "next/link";
import { useState } from "react";
import { usePlans } from "@/app/components/providers/PlanProvider";

export default function AddPage() {
  const { addPlan } = usePlans();

  const [formData, setFormData] = useState({
    profileName: "",
    planTitle: "",
  });

  const handleAddPlan = async () => {
    const { profileName, planTitle } = formData;

    if (!profileName.trim() || !planTitle.trim()) {
      alert("Profile name and plan title are required");
      return;
    }

    try {
      const newProfile = new Profile(profileName);
      const newPlan = new Plan(123123, planTitle, newProfile, []);
      await addPlan(newPlan);
      setFormData({
        profileName: "",
        planTitle: "",
      });
    } catch (error) {
      console.error("Failed to add plan:", error);
      alert("Failed to create plan. Please try again.");
    }
  };

  return (
    <div className="flex h-screen rounded-lg justify-center items-center">
      <div className="flex flex-col bg-lightgrey p-6 rounded-lg items-center">
        <p className="text-white text-2xl font-semibold">Create a Plan</p>
        <div className="flex p-2 rounded-lg items-center">
          <input
            type="text"
            placeholder="Profile Name"
            value={formData.profileName}
            onChange={(e) =>
              setFormData({ ...formData, profileName: e.target.value })
            }
            className="p-2 m-4 border-2 border-lightgreen rounded-lg text-white"
          />
        </div>
        <input
          type="text"
          placeholder="Plan Title"
          value={formData.planTitle}
          onChange={(e) =>
            setFormData({ ...formData, planTitle: e.target.value })
          }
          className="p-2 m-4 border-2 border-lightgreen rounded-lg text-white"
        />
        <div className="flex p-4 w-5/6 gap-4 rounded-lg items-center">
          <Link
            className="text-white w-full bg-lightgrey p-1 rounded-3xl border-2 border-lightgreen font-semibold flex items-center justify-center hover:border-orange transition-all duration-200"
            href="/plans"
            onClick={handleAddPlan}
          >
            Add
          </Link>
        </div>
      </div>
    </div>
  );
}
