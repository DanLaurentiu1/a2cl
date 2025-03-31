import { BaseEdge, EdgeProps, getBezierPath } from "reactflow";

export default function CustomArrowEdge({
  id,
  sourceX,
  sourceY,
  targetX,
  targetY,
  sourcePosition,
  targetPosition,
}: EdgeProps) {
  const edgePadding = -5;
  const adjustedSourceX =
    sourceX +
    edgePadding * Math.cos(Math.atan2(targetY - sourceY, targetX - sourceX));
  const adjustedSourceY =
    sourceY +
    edgePadding * Math.sin(Math.atan2(targetY - sourceY, targetX - sourceX));
  const adjustedTargetX =
    targetX -
    edgePadding * Math.cos(Math.atan2(targetY - sourceY, targetX - sourceX));
  const adjustedTargetY =
    targetY -
    edgePadding * Math.sin(Math.atan2(targetY - sourceY, targetX - sourceX));

  const [edgePath] = getBezierPath({
    sourceX: adjustedSourceX,
    sourceY: adjustedSourceY,
    sourcePosition,
    targetX: adjustedTargetX,
    targetY: adjustedTargetY,
    targetPosition,
  });

  const angle = Math.atan2(targetY - sourceY, targetX - sourceX);

  const arrowSize = 14;

  const arrowPoints = [
    { x: adjustedTargetX, y: adjustedTargetY },
    {
      x: adjustedTargetX - arrowSize * Math.cos(angle - Math.PI / 6),
      y: adjustedTargetY - arrowSize * Math.sin(angle - Math.PI / 6),
    },
    {
      x: adjustedTargetX - arrowSize * Math.cos(angle + Math.PI / 6),
      y: adjustedTargetY - arrowSize * Math.sin(angle + Math.PI / 6),
    },
  ];

  const arrowPath = `M ${arrowPoints[0].x} ${arrowPoints[0].y} L ${arrowPoints[1].x} ${arrowPoints[1].y} L ${arrowPoints[2].x} ${arrowPoints[2].y} Z`;

  return (
    <>
      <BaseEdge
        id={id}
        path={edgePath}
        style={{ stroke: "white", strokeWidth: 2 }}
      />
      <path d={arrowPath} fill="white" />
    </>
  );
}
