import { Plan } from "../../domain/Plan";
import { getProblemById } from "./problems";
import { getProfileByName } from "./profiles";

export const INITIAL_PLANS: Array<Plan> = [
  new Plan(1, "Plan 1", getProfileByName("Profile 1"), [
    [true, getProblemById(1)],
    [true, getProblemById(2)],
    [true, getProblemById(3)],
    [true, getProblemById(4)],
    [false, getProblemById(5)],
    [false, getProblemById(8)],
    [false, getProblemById(12)],
    [false, getProblemById(18)],
  ]),
  new Plan(2, "Plan 2", getProfileByName("Profile 2"), [
    [true, getProblemById(11)],
    [true, getProblemById(12)],
    [false, getProblemById(13)],
    [false, getProblemById(14)],
    [false, getProblemById(15)],
    [false, getProblemById(16)],
    [false, getProblemById(17)],
    [false, getProblemById(18)],
  ]),
  new Plan(3, "Plan 3", getProfileByName("Profile 2"), [
    [true, getProblemById(18)],
    [true, getProblemById(19)],
    [false, getProblemById(20)],
    [false, getProblemById(21)],
    [false, getProblemById(22)],
    [false, getProblemById(23)],
    [false, getProblemById(24)],
    [false, getProblemById(25)],
    [false, getProblemById(26)],
    [false, getProblemById(27)],
    [false, getProblemById(28)],
    [false, getProblemById(29)],
  ]),
  new Plan(4, "Plan 4", getProfileByName("Profile 1"), [
    [true, getProblemById(4)],
    [true, getProblemById(5)],
  ]),
  new Plan(5, "Plan 5", getProfileByName("Profile 2"), [
    [true, getProblemById(18)],
    [true, getProblemById(19)],
    [true, getProblemById(20)],
    [false, getProblemById(21)],
    [false, getProblemById(29)],
  ]),
  new Plan(6, "Plan 6", getProfileByName("Profile 1"), [
    [false, getProblemById(26)],
    [false, getProblemById(27)],
    [false, getProblemById(28)],
    [false, getProblemById(29)],
  ]),
  new Plan(7, "Plan 7", getProfileByName("Profile 1"), [
    [true, getProblemById(1)],
    [true, getProblemById(2)],
    [true, getProblemById(8)],
    [true, getProblemById(9)],
  ]),
  new Plan(8, "Plan 8", getProfileByName("Profile 1"), [
    [true, getProblemById(12)],
    [true, getProblemById(25)],
    [true, getProblemById(26)],
    [false, getProblemById(29)],
  ]),
  new Plan(9, "Plan 9", getProfileByName("Profile 2"), [
    [true, getProblemById(12)],
    [true, getProblemById(25)],
    [true, getProblemById(26)],
    [false, getProblemById(29)],
  ]),
  new Plan(10, "Plan 10", getProfileByName("Profile 2"), [
    [true, getProblemById(12)],
    [true, getProblemById(25)],
    [false, getProblemById(26)],
    [false, getProblemById(29)],
  ]),
] as const;

export function getPlansById(id: number): Plan {
  const result = INITIAL_PLANS.find((plan) => plan.id === id);
  if (result === undefined) {
    throw Error();
  }
  return result;
}
