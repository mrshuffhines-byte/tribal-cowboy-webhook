import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { colors, fonts } from "../theme";

export const Hook: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const fade = spring({ frame, fps, config: { damping: 18 } });
  const slideUp = interpolate(fade, [0, 1], [40, 0]);

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.teal,
        justifyContent: "center",
        alignItems: "center",
        padding: 80,
      }}
    >
      <div
        style={{
          opacity: fade,
          transform: `translateY(${slideUp}px)`,
          textAlign: "center",
          color: colors.cream,
        }}
      >
        <div
          style={{
            fontFamily: fonts.body,
            fontWeight: 300,
            fontSize: 52,
            letterSpacing: 6,
            textTransform: "uppercase",
            color: colors.gold,
            marginBottom: 40,
          }}
        >
          Imagine
        </div>
        <div
          style={{
            fontFamily: fonts.display,
            fontWeight: 700,
            fontSize: 110,
            lineHeight: 1.05,
            color: colors.cream,
          }}
        >
          a pony
          <br />
          writes your class
          <br />
          a letter.
        </div>
      </div>
    </AbsoluteFill>
  );
};
