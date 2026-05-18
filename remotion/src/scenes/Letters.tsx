import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { colors, fonts } from "../theme";

const Envelope: React.FC<{ delay: number; rotate: number }> = ({ delay, rotate }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const enter = spring({
    frame: frame - delay,
    fps,
    config: { damping: 12, mass: 0.6 },
  });
  const lift = interpolate(enter, [0, 1], [80, 0]);

  return (
    <div
      style={{
        width: 380,
        height: 240,
        backgroundColor: colors.cream,
        border: `3px solid ${colors.teal}`,
        borderRadius: 6,
        position: "relative",
        opacity: enter,
        transform: `translateY(${lift}px) rotate(${rotate}deg)`,
        boxShadow: "0 24px 60px rgba(0,0,0,0.25)",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <div
        style={{
          position: "absolute",
          top: -3,
          left: -3,
          right: -3,
          height: 130,
          borderLeft: `190px solid transparent`,
          borderRight: `190px solid transparent`,
          borderTop: `130px solid ${colors.teal}`,
          opacity: 0.15,
        }}
      />
      <div
        style={{
          width: 110,
          height: 110,
          borderRadius: "50%",
          backgroundColor: colors.gold,
          color: colors.teal,
          fontFamily: fonts.display,
          fontWeight: 700,
          fontSize: 28,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          letterSpacing: 1,
          textAlign: "center",
          lineHeight: 1,
          transform: "rotate(-12deg)",
          border: `3px dashed ${colors.teal}`,
        }}
      >
        PONY
        <br />
        POST
      </div>
    </div>
  );
};

export const Letters: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const headlineIn = spring({ frame, fps, config: { damping: 16 } });

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
          fontFamily: fonts.display,
          fontWeight: 700,
          fontSize: 96,
          color: colors.gold,
          textAlign: "center",
          lineHeight: 1.05,
          opacity: headlineIn,
          transform: `translateY(${interpolate(headlineIn, [0, 1], [-30, 0])}px)`,
          marginBottom: 60,
        }}
      >
        4 visits.
        <br />
        3 real letters.
      </div>

      <div
        style={{
          display: "flex",
          gap: 30,
          justifyContent: "center",
          marginBottom: 60,
        }}
      >
        <Envelope delay={15} rotate={-8} />
        <Envelope delay={35} rotate={3} />
        <Envelope delay={55} rotate={-2} />
      </div>

      <div
        style={{
          fontFamily: fonts.body,
          fontWeight: 300,
          fontSize: 38,
          color: colors.cream,
          textAlign: "center",
          maxWidth: 880,
          lineHeight: 1.35,
          opacity: interpolate(frame, [80, 110], [0, 1], { extrapolateRight: "clamp" }),
        }}
      >
        Hand-folded. Hoof-stamped.
        <br />
        Mailed to your classroom between visits.
      </div>
    </AbsoluteFill>
  );
};
