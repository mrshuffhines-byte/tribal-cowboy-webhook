import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { colors, fonts } from "../theme";

export const Title: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleIn = spring({ frame, fps, config: { damping: 14, mass: 0.8 } });
  const taglineIn = spring({ frame: frame - 25, fps, config: { damping: 16 } });
  const lineGrow = interpolate(frame, [10, 50], [0, 400], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.cream,
        justifyContent: "center",
        alignItems: "center",
        padding: 80,
      }}
    >
      <div style={{ textAlign: "center" }}>
        <div
          style={{
            fontFamily: fonts.body,
            fontWeight: 700,
            fontSize: 42,
            letterSpacing: 12,
            textTransform: "uppercase",
            color: colors.amber,
            opacity: titleIn,
            transform: `translateY(${interpolate(titleIn, [0, 1], [30, 0])}px)`,
            marginBottom: 24,
          }}
        >
          Introducing
        </div>
        <div
          style={{
            fontFamily: fonts.display,
            fontWeight: 700,
            fontSize: 180,
            lineHeight: 0.95,
            color: colors.teal,
            opacity: titleIn,
            transform: `scale(${interpolate(titleIn, [0, 1], [0.85, 1])})`,
          }}
        >
          The Pony
          <br />
          Post
        </div>
        <div
          style={{
            width: lineGrow,
            height: 4,
            backgroundColor: colors.gold,
            margin: "40px auto",
          }}
        />
        <div
          style={{
            fontFamily: fonts.display,
            fontStyle: "italic",
            fontSize: 56,
            color: colors.charcoal,
            opacity: taglineIn,
            transform: `translateY(${interpolate(taglineIn, [0, 1], [20, 0])}px)`,
          }}
        >
          Where the pony writes back.
        </div>
      </div>
    </AbsoluteFill>
  );
};
