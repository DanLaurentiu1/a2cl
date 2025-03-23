import { Plan } from "../domain/Plan";
import { Problem } from "../domain/Problem";
import { Profile } from "../domain/Profile";
import { Topic, TopicTypes } from "../domain/Topic";

export class PlanRepository {
  private _plans: Array<Plan>;
  private setPlans: React.Dispatch<React.SetStateAction<Plan[]>> | null = null;

  constructor() {
    this._plans = this.instantiatePlans();
  }

  public initialize(setPlans: React.Dispatch<React.SetStateAction<Plan[]>>) {
    this.setPlans = setPlans;
  }

  public instantiatePlans(): Array<Plan> {
    const arrayTopic: Topic = new Topic(1, "Array", TopicTypes.DataStructures);
    const hashTableTopic: Topic = new Topic(
      2,
      "Hash Table",
      TopicTypes.DataStructures
    );
    const linkedListTopic: Topic = new Topic(
      3,
      "Linked List",
      TopicTypes.DataStructures
    );
    const mathTopic: Topic = new Topic(4, "Math", TopicTypes.Concepts);
    const recursionTopic: Topic = new Topic(
      5,
      "Recursion",
      TopicTypes.Algorithms
    );
    const stringTopic: Topic = new Topic(
      6,
      "String",
      TopicTypes.DataStructures
    );
    const slidingWindowTopic: Topic = new Topic(
      7,
      "Sliding Window",
      TopicTypes.Algorithms
    );
    const divideAndConquerTopic: Topic = new Topic(
      8,
      "Divide And Conquer",
      TopicTypes.Algorithms
    );
    const binarySearchTopic: Topic = new Topic(
      9,
      "Binary Search",
      TopicTypes.Algorithms
    );
    const twoPointersTopic: Topic = new Topic(
      10,
      "Two Pointers",
      TopicTypes.Algorithms
    );
    const dynamicProgrammingTopic: Topic = new Topic(
      11,
      "Dynamic Programming",
      TopicTypes.Concepts
    );

    const problem1: Problem = new Problem(
      1,
      "Two Sum",
      [arrayTopic, hashTableTopic],
      0,
      55
    );
    const problem2: Problem = new Problem(
      2,
      "Add Two Numbers",
      [linkedListTopic, mathTopic, recursionTopic],
      1,
      45
    );
    const problem3: Problem = new Problem(
      3,
      "Longest Substring Without Repeating Characters",
      [hashTableTopic, stringTopic, slidingWindowTopic],
      1,
      36
    );
    const problem4: Problem = new Problem(
      4,
      "Median Of Two Sorted Arrays",
      [arrayTopic, divideAndConquerTopic, binarySearchTopic],
      2,
      43
    );
    const problem5: Problem = new Problem(
      5,
      "Longest Palindromic Substring",
      [dynamicProgrammingTopic, twoPointersTopic, stringTopic],
      1,
      35
    );
    const problem6: Problem = new Problem(
      6,
      "Zigzag Conversion",
      [stringTopic],
      1,
      50
    );

    const proficiencies1 = new Map<Topic, number>([
      [arrayTopic, 75.5],
      [hashTableTopic, 35.5],
      [linkedListTopic, 12.6],
      [mathTopic, 95.4],
      [recursionTopic, 25.5],
      [stringTopic, 84.2],
      [slidingWindowTopic, 84.2],
      [divideAndConquerTopic, 84.2],
      [binarySearchTopic, 84.2],
      [twoPointersTopic, 84.2],
      [dynamicProgrammingTopic, 84.2],
    ]);

    const proficiencies2 = new Map<Topic, number>([
      [arrayTopic, 35.5],
      [hashTableTopic, 12.5],
      [linkedListTopic, 12.6],
      [mathTopic, 92.4],
      [recursionTopic, 78.5],
      [stringTopic, 84.2],
      [slidingWindowTopic, 41.2],
      [divideAndConquerTopic, 24.2],
      [binarySearchTopic, 85.2],
      [twoPointersTopic, 84.2],
      [dynamicProgrammingTopic, 12.8],
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
    return [plan1, plan2, plan3, plan4, plan5];
  }

  addPlan(plan: Plan) {
    this._plans.push(plan);
    this.setPlans?.([...this._plans]);
  }

  getPlans(): Array<Plan> {
    return this._plans;
  }

  getPlanById(id: number) {
    return this._plans.find((plan) => plan.id === id);
  }

  checkProblem(planId: number, problemId: number) {
    const plan = this._plans.find((plan) => plan.id === planId);
    for (let i = 0; i < plan!.problems.length; i++) {
      let [isCompleted, problem] = plan!.problems[i];
      if (problem.id === problemId) {
        isCompleted = !isCompleted;
        break;
      }
    }
    this.setPlans?.([...this._plans]);
  }

  deletePlan(id: number) {
    this._plans = this._plans.filter((plan) => plan.id !== id);
    this.setPlans?.([...this._plans]);
  }
}
export let planRepository = new PlanRepository();
