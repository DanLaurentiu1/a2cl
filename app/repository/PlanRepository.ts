import { Plan } from "../domain/Plan";
import { PlanValidator } from "../validation/PlanValidator";
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
    const plans: Array<Plan> = [];
    plans.push(
      new Plan(
        1,
        "Plan 1",
        this._profileRepository.getProfileByName("Profile 1")!,
        [
          [true, this._problemRepository.getProblemByNumber(1)!],
          [true, this._problemRepository.getProblemByNumber(2)!],
          [false, this._problemRepository.getProblemByNumber(3)!],
        ]
      )
    );
    plans.push(
      new Plan(
        2,
        "Plan 2",
        this._profileRepository.getProfileByName("Profile 2")!,
        [
          [false, this._problemRepository.getProblemByNumber(1)!],
          [true, this._problemRepository.getProblemByNumber(3)!],
          [false, this._problemRepository.getProblemByNumber(5)!],
          [false, this._problemRepository.getProblemByNumber(6)!],
        ]
      )
    );
    plans.push(
      new Plan(
        3,
        "Plan 3",
        this._profileRepository.getProfileByName("Profile 3")!,
        [
          [true, this._problemRepository.getProblemByNumber(1)!],
          [true, this._problemRepository.getProblemByNumber(3)!],
          [true, this._problemRepository.getProblemByNumber(5)!],
          [true, this._problemRepository.getProblemByNumber(3)!],
          [false, this._problemRepository.getProblemByNumber(6)!],
        ]
      )
    );
    plans.push(
      new Plan(
        4,
        "Plan 4",
        this._profileRepository.getProfileByName("Profile 1")!,
        [
          [true, this._problemRepository.getProblemByNumber(1)!],
          [true, this._problemRepository.getProblemByNumber(6)!],
        ]
      )
    );

    plans.push(
      new Plan(
        5,
        "Plan 5",
        this._profileRepository.getProfileByName("Profile 1")!,
        [
          [true, this._problemRepository.getProblemByNumber(1)!],
          [false, this._problemRepository.getProblemByNumber(2)!],
          [true, this._problemRepository.getProblemByNumber(3)!],
          [false, this._problemRepository.getProblemByNumber(6)!],
        ]
      )
    );

    plans.push(
      new Plan(
        6,
        "Plan 6",
        this._profileRepository.getProfileByName("Profile 2")!,
        [
          [true, this._problemRepository.getProblemByNumber(1)!],
          [false, this._problemRepository.getProblemByNumber(2)!],
          [true, this._problemRepository.getProblemByNumber(3)!],
          [false, this._problemRepository.getProblemByNumber(6)!],
          [false, this._problemRepository.getProblemByNumber(7)!],
        ]
      )
    );

    plans.push(
      new Plan(
        7,
        "Plan 7",
        this._profileRepository.getProfileByName("Profile 1")!,
        [
          [false, this._problemRepository.getProblemByNumber(1)!],
          [false, this._problemRepository.getProblemByNumber(2)!],
          [false, this._problemRepository.getProblemByNumber(3)!],
          [false, this._problemRepository.getProblemByNumber(4)!],
          [false, this._problemRepository.getProblemByNumber(7)!],
        ]
      )
    );

    plans.push(
      new Plan(
        8,
        "Plan 8",
        this._profileRepository.getProfileByName("Profile 2")!,
        [
          [true, this._problemRepository.getProblemByNumber(3)!],
          [false, this._problemRepository.getProblemByNumber(4)!],
          [false, this._problemRepository.getProblemByNumber(5)!],
          [false, this._problemRepository.getProblemByNumber(6)!],
          [false, this._problemRepository.getProblemByNumber(7)!],
        ]
      )
    );

    plans.push(
      new Plan(
        9,
        "Plan 9",
        this._profileRepository.getProfileByName("Profile 2")!,
        [
          [false, this._problemRepository.getProblemByNumber(6)!],
          [false, this._problemRepository.getProblemByNumber(7)!],
        ]
      )
    );

    plans.push(
      new Plan(
        10,
        "Plan 10",
        this._profileRepository.getProfileByName("Profile 2")!,
        [
          [false, this._problemRepository.getProblemByNumber(6)!],
          [false, this._problemRepository.getProblemByNumber(8)!],
        ]
      )
    );

    return plans;
  }

  public addPlan(plan: Plan) {
    PlanValidator.validatePlan(plan);
    this._plans.push(plan);
    this.setPlans?.(this._plans);
  }

  public getPlans(): Array<Plan> {
    return this._plans;
  }

  public getPlanById(id: number) {
    return this._plans.find((plan) => plan.id === id);
  }

  public checkProblem(planId: number, problemId: number) {
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

  public deletePlan(id: number) {
    this._plans = this._plans.filter((plan) => plan.id !== id);
    this.setPlans?.(this._plans);
  }
}
export let planRepository = new PlanRepository();
