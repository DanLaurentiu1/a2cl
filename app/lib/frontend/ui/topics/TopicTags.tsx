import { Topic } from "@/app/lib/domain/Topic";

export default function TopicTags({ topics }: { topics: Array<Topic> }) {
  return (
    <div className="flex flex-wrap gap-2">
      {topics.map((topic) => (
        <span
          key={topic.name}
          className="bg-darkgrey text-white text-xs px-3 py-1 rounded-full"
        >
          {topic.name}
        </span>
      ))}
    </div>
  );
}
