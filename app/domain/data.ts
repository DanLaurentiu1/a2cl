import { Topic, TopicTypes } from "./Topic";
import { Profile } from "./Profile";
import { Problem } from "./Problem";
import { Plan } from "./Plan";

const topic1: Topic = new Topic(1, "Binary Tree", TopicTypes.DataStructures);
const topic2: Topic = new Topic(2, "Linked List", TopicTypes.DataStructures);
const topic3: Topic = new Topic(3, "Array", TopicTypes.DataStructures);
const topic4: Topic = new Topic(4, "Matrix", TopicTypes.DataStructures);
const topic5: Topic = new Topic(5, "Trie", TopicTypes.DataStructures);
const topic6: Topic = new Topic(6, "String", TopicTypes.DataStructures);
const problem1: Problem = new Problem(
  1,
  "Problem 1",
  [topic1, topic2, topic3],
  0,
  15
);
const problem2: Problem = new Problem(2, "Problem 2", [topic2, topic6], 1, 25);
const problem3: Problem = new Problem(
  3,
  "Problem 3",
  [topic3, topic5, topic6],
  1,
  85
);
const problem4: Problem = new Problem(4, "Problem 4", [topic1], 0, 20);
const problem5: Problem = new Problem(5, "Problem 5", [], 2, 30);
const problem6: Problem = new Problem(
  6,
  "Problem 6",
  [topic3, topic5, topic6],
  2,
  45
);

const proficiencies1 = new Map<Topic, number>([
  [topic1, 75.5],
  [topic2, 35.5],
  [topic3, 12.6],
  [topic4, 95.4],
  [topic5, 25.5],
  [topic6, 84.2],
]);

const proficiencies2 = new Map<Topic, number>([
  [topic1, 25.5],
  [topic2, 5.5],
  [topic3, 12.6],
  [topic4, 15.4],
  [topic5, 0],
  [topic6, 84.2],
]);

const profile1: Profile = new Profile(1, "Profile 1", proficiencies1, true);
const profile2: Profile = new Profile(2, "Profile 2", proficiencies2, true);

const plan1: Plan = new Plan(1, "Plan 1", profile1, [
  [true, problem1],
  [true, problem2],
  [false, problem3],
]);

const plan2: Plan = new Plan(2, "Plan 2", profile2, [
  [false, problem1],
  [true, problem3],
  [false, problem5],
  [false, problem6],
]);

const plan3: Plan = new Plan(3, "Plan 3", profile2, [
  [true, problem1],
  [true, problem3],
  [true, problem4],
  [true, problem5],
  [false, problem6],
]);

const plan4: Plan = new Plan(4, "Plan 4", profile1, [
  [true, problem1],
  [true, problem6],
]);

const plan5: Plan = new Plan(5, "Plan 5", profile1, [
  [true, problem1],
  [false, problem2],
  [true, problem3],
  [false, problem6],
]);

export let topics = [topic1, topic2, topic3, topic4, topic5, topic6];
export let problems = [
  problem1,
  problem2,
  problem3,
  problem4,
  problem5,
  problem6,
];
export let profiles = [profile1, profile2];
export let plans = [plan1, plan2, plan3, plan4, plan5];
