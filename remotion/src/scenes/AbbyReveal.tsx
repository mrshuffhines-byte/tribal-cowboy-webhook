import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { colors, fonts } from "../theme";

export const AbbyReveal: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const buildUp = spring({ frame, fps, config: { damping: 18 } });
  const ponyScale = interpolate(frame, [0, 60], [1, 0.5], { extrapolateRight: "clamp" });
  const ponyX = interpolate(frame, [0, 60], [0, -260], { extrapolateRight: "clamp" });

  const abbyIn = spring({ frame: frame - 50, fps, config: { damping: 14, mass: 1.2 } });
  const abbyScale = interpolate(abbyIn, [0, 1], [0, 1]);

  const captionIn = interpolate(frame, [110, 140], [0, 1], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.teal,
        justifyContent: "center",
        alignItems: "center",
        padding: 60,
      }}
    >
      <div
        style={{
          fontFamily: fonts.body,
          fontWeight: 700,
          fontSize: 36,
          letterSpacing: 10,
          textTransform: "uppercase",
          color: colors.gold,
          marginBottom: 50,
          opacity: buildUp,
        }}
      >
        Then on the last day
      </div>

      <div
        style={{
          display: "flex",
          alignItems: "flex-end",
          justifyContent: "center",
          gap: 0,
          height: 600,
          width: "100%",
        }}
      >
        <div
          style={{
            fontSize: 280,
            transform: `scale(${ponyScale}) translateX(${ponyX}px)`,
            transformOrigin: "bottom center",
          }}
        >
          🐴
        </div>
        <div
          style={{
            fontSize: 520,
            transform: `scale(${abbyScale})`,
            transformOrigin: "bottom center",
            filter: `drop-shadow(0 10px 30px rgba(0,0,0,0.4))`,
          }}
        >
          🐴
        </div>
      </div>

      <div
        style={{
          textAlign: "center",
          marginTop: 30,
          opacity: captionIn,
          transform: `translateY(${interpolate(captionIn, [0, 1], [20, 0])}px)`,
        }}
      >
        <div
          style={{
            fontFamily: fonts.display,
            fontWeight: 700,
            fontSize: 108,
            color: colors.cream,
            lineHeight: 1,
          }}
        >
          Abby shows up.
        </div>
        <div
          style={{
            fontFamily: fonts.body,
            fontWeight: 300,
            fontSize: 38,
            color: colors.gold,
            marginTop: 20,
            letterSpacing: 2,
          }}
        >
          1,800-lb Clydesdale. Hooves like dinner plates.
        </div>
      </div>
    </AbsoluteFill>
  );
};
