"use client";
import PlanContext from "@/app/context/PlanContext";
import { Plan } from "@/app/lib/domain/Plan";
import { Profile } from "@/app/lib/domain/Profile";
import { Topic } from "@/app/lib/domain/Topic";
import { topicRepository } from "@/app/repository/TopicRepository";
import TopicTags from "@/app/ui/topics/TopicTags";
import Link from "next/link";
import { useContext, useState } from "react";
import { FaPlus } from "react-icons/fa";

export default function AddPage() {
  const context = useContext(PlanContext);

  if (!context) {
    throw new Error("PlansList must be used within a PlanProvider");
  }

  const { planRepository } = context;

  const [topics, setTopics] = useState<Array<Topic>>([]);
  const [profileName, setProfileName] = useState<string>("");
  const [planTitle, setPlanTitle] = useState<string>("");
  const [topicName, setTopicName] = useState<string>("");
  const [fromLeetcode, setFromLeetcode] = useState<boolean>(false);

  const handleAddTopic = () => {
    if (topicName.trim()) {
      if (topicRepository.getTopicByName(topicName)) {
        setTopics([...topics, topicRepository.getTopicByName(topicName)!]);
      }
      setTopicName("");
    }
  };

  const handleAddPlan = () => {
    const newProfile = new Profile(profileName, false);
    const newId = planRepository.getPlans().length;
    const newPlan = new Plan(newId + 1, planTitle, newProfile, []);
    planRepository.addPlan(newPlan);
  };

  return (
    <div className="flex h-screen rounded-lg justify-center items-center">
      <div className="flex flex-col bg-lightgrey p-6 rounded-lg items-center">
        <p className="text-white text-2xl font-semibold">Create a Plan</p>
        <div className="flex p-2 rounded-lg items-center">
          <input
            type="text"
            placeholder="Profile Name"
            value={profileName}
            onChange={(e) => setProfileName(e.target.value)}
            className="p-2 m-4 border-2 border-lightgreen rounded-lg text-white"
          />
          <label className="flex items-center gap-2">
            <input
              type="checkbox"
              checked={fromLeetcode}
              onChange={(e) => setFromLeetcode(e.target.checked)}
              className="w-5 h-5"
            />
            <span className="text-white">From Leetcode</span>
          </label>
        </div>
        <input
          type="text"
          placeholder="Plan Title"
          value={planTitle}
          onChange={(e) => setPlanTitle(e.target.value)}
          className="p-2 m-4 border-2 border-lightgreen rounded-lg text-white"
        />
        <div className="flex p-2 w-full gap-12 rounded-lg items-center">
          <input
            type="text"
            value={topicName}
            onChange={(e) => setTopicName(e.target.value)}
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
