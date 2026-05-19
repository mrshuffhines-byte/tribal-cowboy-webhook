import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { colors, fonts } from "../theme";

const SYLLABLES = ["Ap", "pa", "loo", "sa"];

const Beat: React.FC<{ index: number; pawFrame: number }> = ({ index, pawFrame }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const local = frame - pawFrame;
  const bounce = spring({
    frame: local,
    fps,
    config: { damping: 8, mass: 0.5 },
  });
  const active = local >= 0;
  const scale = active ? interpolate(bounce, [0, 1], [1.6, 1]) : 0.85;
  const opacity = active ? 1 : 0.25;

  return (
    <div
      style={{
        fontFamily: fonts.display,
        fontWeight: 700,
        fontSize: 130,
        color: active ? colors.gold : colors.cream,
        transform: `scale(${scale})`,
        opacity,
        transition: "color 0.2s",
        textAlign: "center",
        minWidth: 200,
      }}
    >
      {SYLLABLES[index]}
    </div>
  );
};

export const SyllablePaw: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const headlineIn = spring({ frame, fps, config: { damping: 16 } });

  // Paws fall on frames 30, 60, 90, 120
  const pawFrames = [30, 60, 90, 120];

  // Hoof shake at the same beats
  const hoofShake = pawFrames.reduce((acc, f) => {
    const local = frame - f;
    if (local >= 0 && local < 8) {
      return acc + Math.sin((local / 8) * Math.PI) * 14;
    }
    return acc;
  }, 0);

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.cream,
        justifyContent: "center",
        alignItems: "center",
        padding: 80,
      }}
    >
      <div
        style={{
          fontFamily: fonts.body,
          fontWeight: 700,
          fontSize: 38,
          letterSpacing: 8,
          textTransform: "uppercase",
          color: colors.amber,
          opacity: headlineIn,
          marginBottom: 30,
        }}
      >
        She paws out syllables
      </div>

      <div
        style={{
          display: "flex",
          gap: 10,
          alignItems: "baseline",
          justifyContent: "center",
          marginBottom: 60,
          opacity: headlineIn,
        }}
      >
        {SYLLABLES.map((_, i) => (
          <Beat key={i} index={i} pawFrame={pawFrames[i]} />
        ))}
      </div>

      <div
        style={{
          fontSize: 240,
          transform: `translateY(${hoofShake}px) rotate(${hoofShake * 0.3}deg)`,
          opacity: headlineIn,
        }}
      >
        🐴
      </div>

      <div
        style={{
          fontFamily: fonts.display,
          fontStyle: "italic",
          fontSize: 44,
          color: colors.teal,
          marginTop: 30,
          opacity: interpolate(frame, [130, 160], [0, 1], { extrapolateRight: "clamp" }),
        }}
      >
        Four beats. One real hoof.
      </div>
    </AbsoluteFill>
  );
};
