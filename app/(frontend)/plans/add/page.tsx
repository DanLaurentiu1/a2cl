"use client";
import { Plan } from "@/app/lib/domain/Plan";
import { Profile } from "@/app/lib/domain/Profile";
import { Topic } from "@/app/lib/domain/Topic";
import { usePlans } from "@/app/lib/frontend/context/PlanProvider";
import TopicTags from "@/app/lib/frontend/ui/topics/TopicTags";
import { getTopicByName } from "@/app/lib/shared/data/topics";
import Link from "next/link";
import { useState } from "react";
import { FaPlus } from "react-icons/fa";

export default function AddPage() {
  const { addPlan } = usePlans();

  const [topics, setTopics] = useState<Array<Topic>>([]);
  const [formData, setFormData] = useState({
    profileName: "",
    planTitle: "",
    topicName: "",
    fromLeetcode: false,
  });

  const handleAddTopic = () => {
    const { topicName } = formData;
    if (topicName.trim()) {
      const topic = getTopicByName(topicName);
      if (topic) {
        setTopics([...topics, topic]);
      }
      setFormData((prev) => ({ ...prev, topicName: "" }));
    }
  };

  const handleAddPlan = async () => {
    const { profileName, planTitle } = formData;

    if (!profileName.trim() || !planTitle.trim()) {
      alert("Profile name and plan title are required");
      return;
    }

    try {
      const newProfile = new Profile(profileName, formData.fromLeetcode);
      const newPlan = new Plan(0, planTitle, newProfile, []);
      await addPlan(newPlan);
      setFormData({
        profileName: "",
        planTitle: "",
        topicName: "",
        fromLeetcode: false,
      });
      setTopics([]);
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
          <label className="flex items-center gap-2">
            <input
              type="checkbox"
              checked={formData.fromLeetcode}
              onChange={(e) =>
                setFormData({ ...formData, fromLeetcode: e.target.checked })
              }
              className="w-5 h-5"
            />
            <span className="text-white">From Leetcode</span>
          </label>
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
        <div className="flex p-2 w-full gap-12 rounded-lg items-center">
          <input
            type="text"
            value={formData.topicName}
            onChange={(e) =>
              setFormData({ ...formData, topicName: e.target.value })
            }
            placeholder="Topic Name"
            className="p-2 m-4 border-2 border-lightgreen rounded-lg text-white"
          />
          <button
            onClick={handleAddTopic}
            className="flex items-center justify-center w-9 h-9 text-white rounded-full border-2 border-lightgreen hover:border-orange transition-all duration-200"
          >
            <FaPlus className="text-base" />
          </button>
        </div>
        <TopicTags topics={topics} />
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
