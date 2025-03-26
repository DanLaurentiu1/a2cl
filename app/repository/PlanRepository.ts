import { Plan } from "../domain/Plan";
import { problemRepository, ProblemRepository } from "./ProblemRepository";
import { profileRepository, ProfileRepository } from "./ProfileRepository";

export class PlanRepository {
  private _plans: Array<Plan>;
  private _problemRepository: ProblemRepository;
  private _profileRepository: ProfileRepository;
  private setPlans: React.Dispatch<React.SetStateAction<Plan[]>> | null = null;

  constructor() {
    this._problemRepository = problemRepository;
    this._profileRepository = profileRepository;
    this._plans = this.instantiatePlans();
  }

  public initialize(setPlans: React.Dispatch<React.SetStateAction<Plan[]>>) {
    this.setPlans = setPlans;
  }

  public instantiatePlans(): Array<Plan> {
    const plan1: Plan = new Plan(
      1,
      "Plan 1",
      this._profileRepository.getProfileByName("Profile 1")!,
      [
        [true, this._problemRepository.getProblemByName("Two Sum")!],
        [true, this._problemRepository.getProblemByName("Add Two Numbers")!],
        [
          false,
          this._problemRepository.getProblemByName(
            "Longest Substring Without Repeating Characters"
          )!,
        ],
      ]
    );

    const plan2: Plan = new Plan(
      2,
      "Plan 2",
      this._profileRepository.getProfileByName("Profile 2")!,
      [
        [false, this._problemRepository.getProblemByName("Two Sum")!],
        [
          true,
          this._problemRepository.getProblemByName(
            "Longest Substring Without Repeating Characters"
          )!,
        ],
        [
          false,
          this._problemRepository.getProblemByName(
            "Longest Palindromic Substring"
          )!,
        ],
        [false, this._problemRepository.getProblemByName("Zigzag Conversion")!],
      ]
    );

    const plan3: Plan = new Plan(
      3,
      "Plan 3",
      this._profileRepository.getProfileByName("Profile 3")!,
      [
        [true, this._problemRepository.getProblemByName("Two Sum")!],
        [
          true,
          this._problemRepository.getProblemByName(
            "Longest Substring Without Repeating Characters"
          )!,
        ],
        [
          true,
          this._problemRepository.getProblemByName(
            "Median Of Two Sorted Arrays"
          )!,
        ],
        [
          true,
          this._problemRepository.getProblemByName(
            "Longest Palindromic Substring"
          )!,
        ],
        [false, this._problemRepository.getProblemByName("Zigzag Conversion")!],
      ]
    );

    const plan4: Plan = new Plan(
      4,
      "Plan 4",
      this._profileRepository.getProfileByName("Profile 1")!,
      [
        [true, this._problemRepository.getProblemByName("Two Sum")!],
        [true, this._problemRepository.getProblemByName("Zigzag Conversion")!],
      ]
    );

    const plan5: Plan = new Plan(
      5,
      "Plan 5",
      this._profileRepository.getProfileByName("Profile 1")!,
      [
        [true, this._problemRepository.getProblemByName("Two Sum")!],
        [false, this._problemRepository.getProblemByName("Add Two Numbers")!],
        [
          true,
          this._problemRepository.getProblemByName(
            "Longest Substring Without Repeating Characters"
          )!,
        ],
        [false, this._problemRepository.getProblemByName("Zigzag Conversion")!],
      ]
    );
    return [plan1, plan2, plan3, plan4, plan5];
  }

  addPlan(plan: Plan) {
    this._plans.push(plan);
    this.setPlans?.(this._plans);
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
        plan!.problems[i][0] = !plan!.problems[i][0];
        break;
      }
    }
    this.setPlans?.(this._plans);
  }

  deletePlan(id: number) {
    this._plans = this._plans.filter((plan) => plan.id !== id);
    this.setPlans?.(this._plans);
  }
}
export let planRepository = new PlanRepository();
