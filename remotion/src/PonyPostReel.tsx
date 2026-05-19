import { AbsoluteFill, Sequence } from "remotion";
import { loadFont as loadPlayfair } from "@remotion/google-fonts/PlayfairDisplay";
import { loadFont as loadLato } from "@remotion/google-fonts/Lato";
import { Hook } from "./scenes/Hook";
import { Title } from "./scenes/Title";
import { Letters } from "./scenes/Letters";
import { SyllablePaw } from "./scenes/SyllablePaw";
import { AbbyReveal } from "./scenes/AbbyReveal";
import { CTA } from "./scenes/CTA";
import { colors } from "./theme";

loadPlayfair();
loadLato();

export const PonyPostReel: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: colors.cream }}>
      <Sequence from={0} durationInFrames={90}>
        <Hook />
      </Sequence>

      <Sequence from={90} durationInFrames={150}>
        <Title />
      </Sequence>

      <Sequence from={240} durationInFrames={180}>
        <Letters />
      </Sequence>

      <Sequence from={420} durationInFrames={180}>
        <SyllablePaw />
      </Sequence>

      <Sequence from={600} durationInFrames={180}>
        <AbbyReveal />
      </Sequence>

      <Sequence from={780} durationInFrames={120}>
        <CTA />
      </Sequence>
    </AbsoluteFill>
  );
};
