import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { colors, fonts } from "../theme";

export const CTA: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const fadeIn = spring({ frame, fps, config: { damping: 18 } });
  const urlIn = interpolate(frame, [30, 60], [0, 1], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.cream,
        justifyContent: "center",
        alignItems: "center",
        padding: 80,
        textAlign: "center",
      }}
    >
      <div
        style={{
          opacity: fadeIn,
          transform: `translateY(${interpolate(fadeIn, [0, 1], [40, 0])}px)`,
        }}
      >
        <div
          style={{
            fontFamily: fonts.display,
            fontWeight: 700,
            fontSize: 88,
            color: colors.teal,
            lineHeight: 1.05,
            marginBottom: 24,
          }}
        >
          Free to schools.
        </div>
        <div
          style={{
            fontFamily: fonts.body,
            fontWeight: 300,
            fontSize: 42,
            color: colors.charcoal,
            lineHeight: 1.4,
            maxWidth: 880,
            marginBottom: 60,
          }}
        >
          Pre-K through 2nd grade.
          <br />
          North Idaho & Eastern Washington.
        </div>
      </div>

      <div
        style={{
          width: 280,
          height: 4,
          backgroundColor: colors.gold,
          margin: "20px 0",
          opacity: urlIn,
        }}
      />

      <div
        style={{
          opacity: urlIn,
          transform: `translateY(${interpolate(urlIn, [0, 1], [20, 0])}px)`,
        }}
      >
        <div
          style={{
            fontFamily: fonts.body,
            fontWeight: 700,
            fontSize: 36,
            letterSpacing: 8,
            textTransform: "uppercase",
            color: colors.amber,
            marginBottom: 16,
          }}
        >
          Sponsor a sprint
        </div>
        <div
          style={{
            fontFamily: fonts.display,
            fontWeight: 700,
            fontSize: 64,
            color: colors.teal,
          }}
        >
          tribalcowboy.com
        </div>
        <div
          style={{
            fontFamily: fonts.body,
            fontWeight: 300,
            fontSize: 28,
            color: colors.gray,
            marginTop: 30,
            letterSpacing: 4,
          }}
        >
          TRIBAL COWBOY · ATHOL, IDAHO
        </div>
      </div>
    </AbsoluteFill>
  );
};
